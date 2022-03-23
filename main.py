from qiskit import QuantumCircuit, Aer, execute


def run_circuit(qc):
    """Runs a given circuit using a simulator

    Args:
        qc (QuantumCircuit): The circuit to be executed

    Returns:
        counts: a list with all the counts for the given circuit
    """
    simulator = Aer.get_backend('qasm_simulator')
    job = execute(qc, simulator, shots=1000)
    result = job.result()
    counts = result.get_counts(qc)
    return counts

def main():
    qc = QuantumCircuit(2, 2)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0,1],[0,1])
    print("\nTotal count for 00 and 11 are:", run_circuit(qc))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
