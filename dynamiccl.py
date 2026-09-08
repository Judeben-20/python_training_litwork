a = list(map(int, input().split()))

if len(a) == 1:
    start = a[0]
    end = 1
else:
    start, end = a

nums = list(range(start, end - 1, -1))

terms = []
even_op = 0
i = 0

while i < len(nums):
    if nums[i] % 2 == 0 and i + 1 < len(nums):

        if even_op % 2 == 0:
            terms.append(nums[i] // nums[i + 1])
        else:
            terms.append(nums[i] * nums[i + 1])

        even_op += 1
        i += 2

    else:
        terms.append(nums[i])
        i += 1

ans = terms[0]

for i in range(1, len(terms)):
    if i % 2 == 1:
        ans += terms[i]
    else:
        ans -= terms[i]

print(ans)