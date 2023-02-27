import pickle

a = {'hello': 'world'}

with open('data.pickle', 'wb') as handle:
    pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('data.pickle', 'rb') as handle:
    b = pickle.load(handle)

print (a == b)
