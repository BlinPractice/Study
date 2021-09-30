# custom_util.py

import os
import shutil

'''
1. 손글씨 숫자 쓰기 (A4 2장)
2. 사진으로 촬영해서 컴퓨터로 복사
3. 동일한 크기로 숫자 추출
   (크기는 각자 정하고, 가로/세로 동일)
4. 압축 파일 업로드
   숫자별 파일 만들어서 저장
5. 데이터 파일 통합
6. 프로젝트 데이터 복사
7. 모델 구축 + 성능 평가
8. 사전 학습 모델 적용'''

'''
Test 2. DL Algorithm Name?
## Regression ##
- Linear Regression
- Multiple Regression
## Classification ##
- Logistic Regression
- Softmax Regression

Test 3. CNN Layer 종류 (크게 3가지)
- Convolution Layer : 피처 추출
- Pooling Layer : 피처 추출
- Dense Layer : 분류

Test 4. DL Accuracy 성능 올릴 수 있는 방법 4가지
- 데이터 증강 (이미지 증강 : AlexNet) augmentation?
- Scaling(Standardization, Normalization)
- Optimization(Adam)
- 3x3 filter 중첩, 1x1 filter 사용
- shortcut connection
- Layer 중첩
- 초기값(glorot, he)
'''


def copy_numbers(root, target):
    root = 'm0'
    target = 'test'

    for i in range(10):
        num_folder = os.path.join(root, str(i))
        dst_folder = os.path.join(target, str(i))
        print(num_folder)

        for idx, filename in enumerate(os.listdir(num_folder)):
            src_path = os.path.join(num_folder, filename)
            dst_path = '{}/{}_{:03}.jpg'.format(dst_folder, root, idx)
            print(src_path, dst_path)
            shutil.copy(src_path, dst_path)
    print('-'*30, root)


for i in range(6):
    copy_numbers(root='m{}'.format(i), target='train')

for i in range(6, 8):
    copy_numbers(root='m{}'.format(i), target='test')
