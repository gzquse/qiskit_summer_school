from qiskit import transpile, execute
from qiskit_aer import AerSimulator
from qiskit.circuit.library import QuantumVolume

sim = AerSimulator(method='statevector', device='GPU')
circ = transpile(QuantumVolume(10, 10, seed = 0))
circ.measure_all()
result = execute(circ, sim, shots=100, blocking_enable=True, blocking_qubits=23).result()