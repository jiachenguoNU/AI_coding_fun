import d2l_torch

device = d2l_torch.device('cuda' if d2l_torch.cuda.is_available() else 'cpu')
print('Using device:', device)
print()

#Additional Info when using cuda
if device.type == 'cuda':
    print(d2l_torch.cuda.get_device_name(0))
    print('Memory Usage:')
    print('Allocated:', round(d2l_torch.cuda.memory_allocated(0)/1024**3,1), 'GB')
    print('Cached:   ', round(d2l_torch.cuda.memory_reserved(0)/1024**3,1), 'GB')