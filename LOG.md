# Log

One entry for each recipe, selection or Track B model you train, newest at
the bottom. The numbers come from `experiments.csv`. "Why" and "what it means"
are in your own words: your agent asks you for them and does not make them up.
End the log with your plan for what to try next.

<!-- The form of an entry:

## <date> <tag> (Track A or B)
- changed: what is different from the run before
- why: your reason
- validation: 0.000 (before: 0.000)
- what it means: what you think the result says
-->

## 2026-11-03 baseline (Track A)
- changed: nothing, the starter recipe on all training photos, trained with seeds 0 and 1 on Colab
- why: 기존 레시피를 같은 seed로 두 번 돌리게 될 경우, 사진을 보여주는 순서, 사진을 자르는 위치 등의 값이 같으므로 거의 똑같은 점수가 나와 학습의 이유가 사라진다. 다른 seed로 기존 레시피를 돌리게 될 경우엔 앞서 말했던 값들이 무작위로 달라져 점수의 차이가 생기게 된다. 운이 좋을 경우엔 높은 점수가, 반대로 운이 안 좋을 경우엔 낮은 점수가 나오게 되므로 운 때문에 변동하는 점수의 값을 파악할 수 있다. 
- validation: seed 0 0.4954, seed 1 0.4917 (difference -0.0037)
  - seed 0: seoul 0.5647, busan 0.3813, tokyo 0.6344, osaka 0.3398, taipei 0.5568
  - seed 1: seoul 0.5552, busan 0.3863, tokyo 0.6125, osaka 0.3811, taipei 0.5234
- mistakes sheets (seed 0 model, every second validation photo):
  1. 주변에 뭐가 없는 황량한 도로 사진. 길거리 사진은 맞으나 지역이 특정될 만한 요소 없음.
  2. 한국의 절, 일본의 신사, 대만의 사당과 같은 동양의 종교 건축물들의 구분을 어려워 함.
  3. 서울/부산, 도쿄/오사카 끼리는 서로 같은 나라에 속해있는 지역이라 구분을 어려워 함.
  4. 자동차 사진이 많이 들어가있고, 구분을 어려워 함. 
  5. 전통 건축물이 아닌 현대식 건물 단독 사진 구분을 어려워 함.
  6. 층이 높은 건축물들은 대체로 서울, 층이 낮은 건축물들은 대체로 도쿄로 잘못 지시했음.
  7. 영어가 크게 나온 사진은 서울로, 한자가 크게 나온 사진은 오사카로 인식하는 경향을 보임. 한글이 나온 사진은 오사카로 인식함.
- what it means: seed 0과 seed 1의 전체 점수 차는 약 0.4로 그닥 크다고 할 수 없다. 그저 seed 0의 운이 아주 조금 더 좋았다고 말할 수 있다. 다만 도시별 점수를 확인하면 이야기가 달라진다. 오사카는 seed 1이 seed 0보다 점수가 약 4점 정도 높고 타이베이는 약 3점 정도 낮은 걸 보면 운에 따라 꽤나 유의미한 점수 차이가 있다는 걸 확인할 수 있다. 따라서 앞으로 실험을 진행할 때, 특정 도시만 5점 미만으로 점수가 올랐다면 이는 효과라고 판단하기 어렵다. 단순히 운이 작용했을 수도 있기 때문이다.

## 2026-11-05 rule for dropping training photos
- rule: 도시를 특정할 단서가 없는 학습 사진은 뺀다. 구체적으로 ① 주변에 아무것도 없는 황량한 길 사진, ② 자동차가 화면 대부분을 차지해 배경이 거의 안 보이는 사진.
- reason: 학습 전에 각 도시의 특징 파악을 위해 각각의 사진 폴더를 검사하는데, 부산의 사진 폴더에 유독 자동차 사진이 많은 것을 확인할 수 있었다. 모델이 '자동차가 보이면 -> 부산'과 같이 잘못된 판단을 할 수 있으므로 자동차가 화면에 꽉 들어찬 사진은 제외하도록 한다. 또, 도시 사진 폴더에서 공통적으로 '도로만 크게 나온 사진'이 많이 발견되었고 이는 모델이 특정 도시를 판단하기 어렵게 만들기에 제외하도록 한다.
- revised rule: 기존 규칙 '① 주변에 아무것도 없는 황량한 길 사진 제거하기 ② 자동차가 화면 대부분을 차지해 배경이 거의 안 보이는 사진 제거하기'에서 규칙 ②만 남긴다.
- why I revised it: 규칙 ①과 ②를 동시에 고려하려고 하니 판단 시간이 오래 걸린다. 고로 여러 사진을 검토할 여유가 없다. 규칙 ②의 특징이 도드라지는 부산은 5장에 1장씩, 22장 시트를 만들어 검토하고, 다섯 도시 전부 suspects를 도시별로 48장씩 뽑아 검토했으나 총 59장의 사진밖에 제거하지 못하였다. 이는 전체 사진 수에 비해 턱없이 적은 수라 판단해 조건을 ② 하나로 수정하고 더 많은 사진을 검토해 학습력을 높이고자 한다.
- 버스가 사진에 꽉 찼는데 글씨가 안 보이면 -> 규칙 ②에 맞음
- 버스에 한글·한자·영어가 잘 보이면 → 규칙 ②에 틀림
- 규칙 ②의 특징이 도드라지는 부산은 사진 전부를 확인(나의 눈으로)해 규칙에 적합한 사진을 제거했고, 나머지 도시들은 사진들을 전부 검사해서 각 도시별로 suspects를 240장을 뽑아 규칙에 적합한 사진을 제거하였다.

## 2026-11-05 drop_car_closeups (Track A)
- changed: training photos selected by rule ② (자동차가 화면 대부분을 차지해 배경이 거의 안 보이는 사진), 174 photos dropped from the 44257 starter training photos; same starter recipe, seed 0, on Colab
  - sheets looked at and photos dropped from each:
    - `look busan --every 5` (every 5th Busan photo, 22 sheets): 30 dropped (look_busan_02: 21, look_busan_03: 9)
    - `suspects` on baseline_seed0, `--every 4` (48 per city, one sheet per city): 3 dropped (taipei_00: 1, tokyo_00: 2)
    - `look busan` on every selected Busan photo (108 sheets): 121 dropped (look_busan_25: 1, look_busan_94: 12, look_busan_95: 48, look_busan_96: 48, look_busan_97: 12)
    - `suspects` on baseline_seed0 on every selected photo, `--n 240` (5 sheets per city; Seoul, Tokyo, Osaka and Taipei looked at): 20 dropped (seoul 1, tokyo 5, osaka 7, taipei 7)
  - 26 photos dropped earlier by rule ① were put back when the rule was revised
  - final selection: 44083 photos (seoul 11273 of 11274, busan 5040 of 5191, tokyo 13340 of 13347, osaka 7193 of 7200, taipei 7237 of 7245)
- why: 학습 전에 각 도시의 특징 파악을 위해 각각의 사진 폴더를 검사하는데, 부산의 사진 폴더에 유독 자동차 사진이 많은 것을 확인할 수 있었다. 모델이 '자동차가 보이면 -> 부산'과 같이 잘못된 판단을 할 수 있으므로 자동차가 화면에 꽉 들어찬 사진은 제외하도록 한다.
- validation: 0.4983 (before: baseline seed 0 0.4954, seed 1 0.4917)
  - drop_car_closeups: seoul 0.5667, busan 0.3820, tokyo 0.6503, osaka 0.3670, taipei 0.5252
  - baseline seed 0:   seoul 0.5647, busan 0.3813, tokyo 0.6344, osaka 0.3398, taipei 0.5568
  - baseline seed 1:   seoul 0.5552, busan 0.3863, tokyo 0.6125, osaka 0.3811, taipei 0.5234
- what it means: 전체 점수는 0.4983으로 기준점인 Seed 0보다는 0.0029 높게 나왔다. 하지만 이것은 처음에 seed 0과 seed 1로 운을 측정했을 때, 생긴 전체 차이(0.0037)보다 작은 값으로 개선되었다고 보기 어렵다. 

  더 많은 양의 Suspects 사진을 검토하며 깨닫게 된 사실은 자동차 사진이 나의 예상보다 많이 없었다는 점이다. Suspects 시트 한 장에 자동차 하나도 없을 때가 빈번했다. 사람인 나에게 자동차 사진은 도시를 구분할 단서가 부족하다고 느껴졌지만, AI에게는 내가 발견하지 못한 단서들이 있었나보다. 전체 사진을 검토하고, 가장 많은 사진을 뺀(151장) 부산의 점수는 거의 변하지 않은 걸 보면 자동차 사진은 부산의 점수를 낮추는 원인이 아닌 걸 알 수 있다. 도쿄는 1.6~3.8점이 올랐는데 이것또한 처음에 운 때문에 변동되는 점수 폭(약 4점)보다 작았기에 의미있는 결과로 보기 어렵다. 

## 2026-11-05 b_starter (Track B)
- changed: the starter `train_b.py` as given (`--tag b_starter --submit`): resnet18 at 224 from torchvision IMAGENET1K_V1, 4 epochs, on all 44257 starter training photos (seoul 11274, busan 5191, tokyo 13347, osaka 7200, taipei 7245), on Colab; 11.17 million parameters, 1.81 billion multiply-adds; check_submission: format and limits: OK
- why: Track B는 Track A와 비교했을 때, 커스텀이 매우 자유롭다. 학습코드, 이미지 크기, 모델(파라미터 수의 크기 제한은 있다), 심지어 기존 사진에 추가로 내가 선별한 사진을 추가할 수도 있다. 전부 내가 결정하는 것에 따라 점수가 움직인다. Track A는 학습방식이 다르기에 기준점으로 삼을 수 없다. 따라서, 내 점수를 채점하기 위한 기준값이 바로 b_starter가 되겠다.
- validation: 0.4943 (before: none, the first Track B model)
  - seoul 0.5655, busan 0.4000, tokyo 0.6251, osaka 0.3661, taipei 0.5149
- what it means: Track B의 전체 기준값은 0.4943이 나왔고 가장 헷갈려하는 도시는 순서대로 오사카와 부산으로 Track A와 비슷한 결과가 나왔다. 아직 현재까지는 Track A와 같은 모델을 쓰고 있고 스타터 사진또한 일치해서 그런가보다. 

## 2026-11-08 b_mnv3_320 and b_mnv3_512 (Track B)
- changed: mobilenet_v3_large (torchvision IMAGENET1K_V2) instead of resnet18, at 320 (b_mnv3_320) and at 512 (b_mnv3_512); everything else as in b_starter (4 epochs, all starter photos, learning rate 3e-4, batch size 64); 4.20 million parameters, 0.44 billion multiply-adds at 320 and 1.11 billion at 512
- why: 기존 사용하던 모델보다 성능(ImageNet 정확도)이 더 높은 모델이고 크기도 더 작아 연산량도 적다. 사진의 크기가 커져서 계산이 늘어나도 모델이 덜 복잡하기에 연산량의 제한에 걸리지 않는다. 사진을 더 큰 픽셀로 선명하게 볼 수 있다면 이전에 뭉개지던 사진 속 글씨들도 단서로 활용할 수 있을 것이리라 기대한다. 지금 실험에선 모델과 픽셀 크기를 동시에 바꾸어 점수 차이가 무엇 때문에 일어난 건지 파악이 어렵기에 바꾼 모델로 픽셀 크기가 320일 때와, 512일 때를 비교해보기로 했다.

## Next plan
Track B에선 사진을 직접 추가해볼 예정이다. 실내 사진은 제외하고 철저히 실외 사진으로 배경 중심에 사진을 선별해 넣으면 학습이 수월하지 않을까 생각한다. 물론 도시당 사진 몇십장만으로는 효과가 미미할 거라고 생각해 추가할 사진의 양도 늘리고, 도시일 확률 0.3 이하인 사진을 suspects 시트로 만들어 전부 검토한 다음, 도시를 특정하기 어려운 대상 중심의 음식 사진, 셀카 등을 스타터 사진에서 제외해볼 예정이다. 
