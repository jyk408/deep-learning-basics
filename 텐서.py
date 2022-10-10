"""
텐서(Tensor)
  - 텐서는 배열이나 행렬과 유사한 자료구조이다
  - 'GPU'나 다른 하드웨어 가속기에서 실행할 수 있는 점만 제외하면 Numpy의  ndarray와 유사하다

"""

import torch
import numpy as np

# 텐서 초기화

## 데이터로 부터 직접 생성
data = [
    [1, 2],
    [3, 4]
]
x_data = torch.tensor(data)
print(x_data)

## Numpy 배열로부터 생성
np_array = np.array(data)
x_np = torch.from_numpy(np_array)
print(x_np)

## 다른 tensor로 부터 받아와 생성
x_ones = torch.ones_like(x_data)
print(x_ones)
x_ones = torch.ones_like(x_data, dtype=torch.float) # x_data의 데이터 속성을 override
print(x_ones)

## random 또는 상수(constant)값을 이용해 생성
shape = (2,  3, )
rand_tensor = torch.rand(shape)
zeros_tensor = torch.zeros(shape)
ones_tensor = torch.ones(shape)
print(rand_tensor)
print(zeros_tensor)
print(ones_tensor)

# 텐서의 속성(attribute): 텐서의 모양(shape), 자료형(datatype)및 어느 장치에 저장되는지를 나타낸다
tensor = torch.rand(3, 4)
print(tensor.shape) # 텐서의 차원
print(tensor.dtype) # 텐서 데이터 타입
print(tensor.device)

# 텐서의 연산 (operation): 전치(transposing), 인덱싱, 슬라이싱, 수학계산, 선형대수, random sampling 등의 기능 포함
# 기본적으로 텐서는 CPU에 생성이 되기 때문에 gpu생성으로 명시 변환 필요

# GPU 존재하면 텐서를 이동
if torch.cuda.is_available():
    tensor = torch.to('cuda')

# numpy식 표준 인덱싱과 슬라이싱
print(tensor[0])
print(tensor[:, 0])
print(tensor[..., -1])




