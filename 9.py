s = [{input() for j in range(int(input()))} for i in range(int(input()))]
known_by_everyone, known_by_someone = set.intersection(*s), set.union(*s)
print(len(known_by_everyone), *sorted(known_by_everyone), sep='\n')
print(len(known_by_someone), *sorted(known_by_someone), sep='\n')
