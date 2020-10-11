a = 1
triples = []
END = 10500

def pairs(n):
    return [(i, n / i) for i in range(1, int(n**0.5) + 1) if n % i == 0]


while a < END:
	fp = pairs(a*a)
	for p in fp:
		s = p[1]+p[0]
		d = p[1] - p[0]
		if s % 2 == 1 or d == 0:
			continue
		c = int(s/2)
		b = int(d/2)
		if a < b:
			triples.append((a,b,c))
	a += 1

o = ""

for t in triples:
	o += str(t)[1:-1] + "\n"

f = open("./out.csv", "w+")
f.write(o)

print("Generated "+ str(len(triples)) + " Pythagorean triples.")
