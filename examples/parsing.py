import dataclasses
from typing import Callable, Iterable, Optional, Set

import innertube
import roster
from innertube.models import ResponseFingerprint


@dataclasses.dataclass
class Target:
    request: Set[str] = dataclasses.field(default_factory=set)
    function: Set[str] = dataclasses.field(default_factory=set)
    browse_id: Set[str] = dataclasses.field(default_factory=set)
    context: Set[str] = dataclasses.field(default_factory=set)
    client: Set[str] = dataclasses.field(default_factory=set)

    @classmethod
    def from_response_fingerprints(cls, *response_fingerprints: ResponseFingerprint):
        parser = cls()

        response_fingerprint: ResponseFingerprint
        for response_fingerprint in response_fingerprints:
            key: str
            value: str
            for key, value in dataclasses.asdict(response_fingerprint).items():
                if value is not None:
                    getattr(parser, key).add(value)

        return parser

    def keys(self) -> Iterable[str]:
        return dataclasses.asdict(self).keys()

    def values(self) -> Iterable[str]:
        return dataclasses.asdict(self).values()

    def any(self) -> bool:
        return any(self.values())

    def all(self) -> bool:
        return all(self.values())

    def intersect(self, rhs):
        parser = type(self)()

        key: str
        value: str
        for key, value in dataclasses.asdict(self).items():
            if value in getattr(rhs, key):
                getattr(parser, key).add(value)

        return parser

    def union(self, rhs):
        parser = type(self)()

        for child in (self, rhs):
            key: str
            value: str
            for key, value in dataclasses.asdict(child).items():
                getattr(parser, key).add(value)

        return parser


parsers: roster.Register[Callable[[dict], dict], Target] = roster.Register()

parser: Callable = parsers.value(Target)


@parser(request=innertube.Request.CONFIG)
def parse_config(data: dict) -> dict:
    print("PARSING:", data)

    return data


client: innertube.Client = innertube.Client(
    adaptor=innertube.InnerTubeAdaptor(
        context=innertube.ClientContext("WEB_REMIX", "0.1")
    )
)


@client.middleware
def parse(call_next, data):
    fingerprint: Optional[innertube.ResponseFingerprint] = innertube.fingerprint(data)

    if fingerprint is None:
        raise Exception("Can't fingerprint data")

    fingerprint_target: Target = Target.from_response_fingerprints(fingerprint)

    parse: Callable[[dict], dict]
    target: Target
    for parse, target in reversed(parsers.items()):
        if not target.any() or target.intersect(fingerprint_target).any():
            return call_next(parse(data))

    raise Exception(f"No parser found for response with fingerprint: {fingerprint!r}")


data: dict = client(innertube.Endpoint.CONFIG)
