from scipy.io import loadmat
import numpy as np

data_file = 'data.mat'
Nelem = 320
Ndof = 810
Nnode = 8

Nsample = 1

Max_iter = 100
Alpha = 0.01
Lambda = 0.001


def get_data(data_file):
    data = loadmat(data_file)

    X_train = data['X_train']
    Y_train = data['Y_train']

    X_test = data['X_test']
    Y_test = data['Y_test']

    return X_train, Y_train, X_test, Y_test


def sample(select):
    new_select_all = []

    target = np.arange(Nelem)
    target_remove = np.asarray(select)
    for i in range(target_remove.shape[0]):
        index = np.argwhere(target == target_remove[i])
        target = np.delete(target, index)

    s = np.random.choice(target, Nsample, replace=False)

    for i in range(s.shape[0]):
        ss = select.copy()
        ss.append(s[i])
        new_select_all.append(ss)

    return new_select_all


def trim_data(X, select):
    select = np.asarray(select)
    n = select.shape[0]

    n1, n2, n3 = X.shape
    X_trim = np.reshape(X[:, select, :].transpose((1, 0, 2)), (n1 * n, n3))

    return X_trim


def train_select(X_train, Y_train):
    n, m = X_train.shape
    N = Y_train.shape[0]

    # W = np.ones((N, n)) * 0.001
    W = np.random.uniform(-0.001, 0.001, (N, n))
    b = np.zeros((N, ))
    for i in range(Max_iter):
        index = np.random.permutation(m)
        # dW = 0
        # for j in range(m):
        #     fe = X_train[:, index[j]]
        #     f = Y_train[:, index[j]]
        #     dW += np.outer(f - W @ fe, -fe)
        # dW += Lambda * W
        # W -= Alpha * dW
        for j in range(m):
            fe = X_train[:, index[j]]
            f = Y_train[:, index[j]]
            dW = np.outer(f - W @ fe - b, -fe) + Lambda * W
            db = -(f - W @ fe - b) + Lambda * b
            W -= Alpha * dW
            b -= Alpha * db
        # train_e = np.linalg.norm(Y_train - W @ X_train, 'fro') ** 2
        print(np.vstack((Y_train[60:61,55], (W @ X_train + b[:, np.newaxis])[60:61,55])))
        # print('Iteration ' + str(i) +
        #       ', train error = ' + str(train_e))

    return W, b


def test_select(X_test, Y_test, W, b):
    e = np.linalg.norm(Y_test - W @ X_test - b[:, np.newaxis], 'fro')
    rel_e = e / np.linalg.norm(Y_test, 'fro')
    print('Test error = ' + str(rel_e))


def find_best_select(X_train, Y_train, X_test, Y_test, select_all):
    for i in range(len(select_all)):
        print('\nTrain on ' + str(select_all[i]))
        W, b = train_select(trim_data(X_train, select_all[i]), Y_train)
        test_select(trim_data(X_train, select_all[i]), Y_train, W, b)

    return 0


def main():
    X_train, Y_train, X_test, Y_test = get_data(data_file)

    select = [0, 50, 100, 150, 200, 250, 300]
    new_select_all = sample(select)

    new_select = find_best_select(X_train, Y_train, X_test, Y_test, new_select_all)






if __name__ == '__main__':
    main()
