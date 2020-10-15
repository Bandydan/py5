жожц	в
цжуоарщцоуат
qwklfbhqwpijef
wifbwpef
qw;lfhjwdfn;qw;d = {
	"Ivanoff": [1, 2, 3, 2, 1, 2, 4, 3, 2],
	"Petroff": [4, 5, 6, 5, 4],
	"Sidoroff": [7, 8, 9, 5, 6, 7]
}

def maxmin(rangs):
	mmax = 0
	mmin = 100000
	maxkey = minkey = ''

	for key, val in rangs.items():
		if (sum(val)/len(val) > mmax):
			mmax = sum(val)/len(val)
			maxkey = key
		if (sum(val)/len(val) < mmin):
			mmin = sum(val)/len(val)
			minkey = key

	return {'max': (maxkey, mmax), 'min': (minkey, mmin)}

print(maxmin(d))
