# Quantum Fourier Transform (QFT) in Qrisp
import qrisp as q
n = 6
qv = q.QuantumVariable(n)
q.QFT(qv)
print(qv.qs)