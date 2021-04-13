import addict

class Dict(addict.Dict):
    def filter(self, function = None):
        if not function:
            function = lambda _, value: value is not None \
                and (not isinstance(value, addict.Dict) or value)

        return \
        {
            key: value
            for key, value in self.items()
            if function(key, value)
        }
