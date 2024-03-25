class Tensor:
    def __init__(self, rows, cols, data):
        self.rows = rows
        self.cols = cols
        self.data = data



def read_tensor_from_file(file_path):
    with open(file_path, 'r') as file:
        rows, cols = map(int, file.readline().strip().split())
        data = []
        for _ in range(rows):
            row = list(map(float, file.readline().strip().split()))
            data.append(row)
    return Tensor(rows, cols, data)

def tensor_product(*tensors):
    if len(tensors) < 2:
        raise ValueError("At least two tensors are required for tensor product.")

    # Compute the tensor product iteratively
    result = tensors[0]
    for tensor in tensors[1:]:
        result = compute_tensor_product(result, tensor)

    return result

def compute_tensor_product(tensor1, tensor2):
    # Compute the dimensions of the resulting tensor
    rows = tensor1.rows * tensor2.rows
    cols = tensor1.cols * tensor2.cols

    # Initialize an empty array to store the data of the resulting tensor
    data = []

    # Compute the data for the resulting tensor
    for i in range(tensor1.rows):
        for j in range(tensor1.cols):
            for m in range(tensor2.rows):
                for n in range(tensor2.cols):
                    data.append(tensor1.data[i][j] * tensor2.data[m][n])

    # Create a new Tensor object for the resulting tensor
    result_tensor = Tensor(rows=rows, cols=cols, data=data)

    return result_tensor


def write_tensor_to_file(tensor, file_path):
    with open(file_path, 'w') as file:
        file.write(f"{tensor.rows} {tensor.cols}\n")
        if isinstance(tensor.data[0], list):
            # If tensor.data is a list of lists (matrix format)
            for j in range(tensor.cols):
                column = [tensor.data[i][j] for i in range(tensor.rows)]
                file.write(" ".join(map(str, column)) + "\n")
        else:
            # If tensor.data is a flat list
            for i in range(tensor.rows):
                row = tensor.data[i * tensor.cols: (i + 1) * tensor.cols]
                file.write(" ".join(map(str, row)) + "\n")













# Example usage
tensor1 = read_tensor_from_file('tensor1.txt')
tensor2 = read_tensor_from_file('tensor2.txt')

result_tensor = tensor_product(tensor1, tensor2)

print("Tensor Product:")
print(result_tensor)

write_tensor_to_file(result_tensor, 'result_tensor.txt')
