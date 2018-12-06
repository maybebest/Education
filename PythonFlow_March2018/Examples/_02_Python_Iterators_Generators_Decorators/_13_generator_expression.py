"""Generator Expression"""


def gen_factory():
    for x in range(10):
        if x % 2 == 0:
            yield x ** 2


GEN_EXP = (x ** 2 for x in range(10) if x % 2 == 0)

GENERATOR_FACTORY = gen_factory()

print(next(GEN_EXP), next(GENERATOR_FACTORY))
# 0 0

print(next(GEN_EXP), next(GENERATOR_FACTORY))
# 4 4

print(next(GEN_EXP), next(GENERATOR_FACTORY))
# 16 16

for e in GEN_EXP:
    print(e)  # 36, 64
