Title: How to make a nested dictionary in Python 3
Date: 2025-05-05 16:08
Modified: 2025-05-05 16:08
Tags: recipes, Python
Category: Python
Slug: autovivify
Authors: aekazakov
Summary: Auto-vivification in Python 3

This function creates a nested dictionary with an assigned value type for the deepest level subkeys.
Thoug I use this function for many years, I am not an author of it.  

```
from collections import defaultdict

def autovivify(levels=1, final=dict):
    return (defaultdict(final) if levels < 2 else
            defaultdict(lambda: autovivify(levels - 1, final)))
```
