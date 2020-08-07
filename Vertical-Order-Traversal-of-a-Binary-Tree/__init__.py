class Solution:
    def set_vertical_distancing(self, root):
        dictionary = {}

        def _set_vertical_distancing(r, distance=0, level=0):
            if r is None:
                return

            dictionary.setdefault(level, {}).setdefault(distance, []).append(r.val)

            _set_vertical_distancing(r.left, distance - 1, level + 1)
            _set_vertical_distancing(r.right, distance + 1, level + 1)

        _set_vertical_distancing(root)

        return dictionary

    def verticalTraversal(self, root):
        dictionary = self.set_vertical_distancing(root)

        result = {}

        for k, v in dictionary.items():
            for k1, v1 in v.items():
                result.setdefault(k1, []).extend(sorted(v1))

        return [
            v
            for k, v in sorted(result.items(), key=lambda x: x[0])
        ]
