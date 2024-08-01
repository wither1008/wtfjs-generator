import random

examples = ["[] is equal ![] https://github.com/denysdovhan/wtfjs?tab=readme-ov-file#-is-equal-",
            "true is not equal ![], but not equal [] too https://github.com/denysdovhan/wtfjs?tab=readme-ov-file#true-is-not-equal--but-not-equal--too",
            "true is false https://github.com/denysdovhan/wtfjs?tab=readme-ov-file#true-is-false",
            "[] is truthy, but not true https://github.com/denysdovhan/wtfjs?tab=readme-ov-file#-is-truthy-but-not-true",
            "null is falsy, but not false https://github.com/denysdovhan/wtfjs?tab=readme-ov-file#null-is-falsy-but-not-false",
            "document.all is an object, but it is undefined https://github.com/denysdovhan/wtfjs?tab=readme-ov-file#documentall-is-an-object-but-it-is-undefined",
            "NaN is not a NaN https://github.com/denysdovhan/wtfjs?tab=readme-ov-file#nan-is-not-a-nan",
            "function is not a function https://github.com/denysdovhan/wtfjs?tab=readme-ov-file#function-is-not-a-function",
            "{}{} is undefined https://github.com/denysdovhan/wtfjs?tab=readme-ov-file#-is-undefined"]
def wtfjs():
    return examples[random.randint(0, len(examples)-1)]