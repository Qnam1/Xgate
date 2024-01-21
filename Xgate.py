from qiskit import QuantumCircuit, execute, Aer

# Create a quantum circuit with 4 qubits
circuit = QuantumCircuit(4)

# Apply HXXH gate to qubits 0 and 1
circuit.h(0)
circuit.x(0)
circuit.x(1)
circuit.h(1)

# Apply Algermatic gate to qubits 2 and 3
circuit.cx(2, 3)
circuit.cz(2, 3)
circuit.x(2)
circuit.cz(2, 3)
circuit.x(2)

# Measure all qubits
circuit.measure_all()

# Simulate the circuit
simulator = Aer.get_backend('qasm_simulator')
job = execute(circuit, simulator, shots=1000)
result = job.result()

# Get the counts of the measurement outcomes
counts = result.get_counts(circuit)
