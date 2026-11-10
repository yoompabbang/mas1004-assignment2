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
- changed: mobilenet_v3_large instead of resnet18, at 320 (b_mnv3_320) and at 512 (b_mnv3_512); everything else as in b_starter (4 epochs, all 44257 starter photos, learning rate 3e-4, batch size 64), on Colab, with `--keep` so that both models came back
  - starting weights differ: b_starter used torchvision resnet18 IMAGENET1K_V1, both MobileNetV3 runs used torchvision mobilenet_v3_large IMAGENET1K_V2
  - 4.20 million parameters; 0.44 billion multiply-adds at 320 and 1.11 billion at 512; check_submission: format and limits: OK for both
  - training time: b_mnv3_320 2444.7 s (40.7 min), b_mnv3_512 4531.1 s (75.5 min); b_starter took 1899.7 s (31.7 min)
- why: 기존 사용하던 모델보다 성능(ImageNet 정확도)이 더 높은 모델이고 크기도 더 작아 연산량도 적다. 사진의 크기가 커져서 계산이 늘어나도 모델이 덜 복잡하기에 연산량의 제한에 걸리지 않는다. 사진을 더 큰 픽셀로 선명하게 볼 수 있다면 이전에 뭉개지던 사진 속 글씨들도 단서로 활용할 수 있을 것이리라 기대한다. 지금 실험에선 모델과 픽셀 크기를 동시에 바꾸어 점수 차이가 무엇 때문에 일어난 건지 파악이 어렵기에 바꾼 모델로 픽셀 크기가 320일 때와, 512일 때를 비교해보기로 했다.
- validation: b_mnv3_320 0.5494, b_mnv3_512 0.5644 (before: b_starter 0.4943)
  - b_mnv3_320: seoul 0.6144, busan 0.4540, tokyo 0.6774, osaka 0.4008, taipei 0.6005
  - b_mnv3_512: seoul 0.6563, busan 0.4022, tokyo 0.6418, osaka 0.4478, taipei 0.6741
  - b_starter:  seoul 0.5655, busan 0.4000, tokyo 0.6251, osaka 0.3661, taipei 0.5149
- what it means: 우선 모델을 바꾸자 전체 점수가 b_starter에 비해 약 5.5~7점 상승했다. Track A에서 확인한 운의 크기(전체 약 0.4점)에 비하면 10배 이상 큰 변화이다. 확실히 효과가 있었다. 물론 같은 모델에서 픽셀 크기가 224일 때와 512일 때를 비교한 건 아니라, 오직 모델만이 점수 향상에 영향을 미쳤다고 말할 순 없다. 픽셀 크기가 320일 때와 512일 때를 비교하면, 픽셀 크기가 512일 때가 전체 점수가 약 1.5점이나 더 높지만 도시별로 비교에 들어가면 픽셀 크기가 320일 때는 모든 도시가 고르게 점수가 오른 반면, 픽셀 크기가 512일 때는 특정 도시(서울, 오사카, 타이베이)의 점수 변화가 큰 것을 확인할 수 있었다. 특히 눈에 띄는 건 픽셀 크기를 키웠을 때 같은 나라의 다른 도시(서울-부산/도쿄-오사카)의 점수 변화 방향이 반대였다는 점이다. 부산에서 헷갈리는 사진을 서울로 몰아주게 된 것이 아닐까. 픽셀 크기가 512일 때는 계산 또한 오래 걸리고, 각 도시 별로 점수의 편차가 고르지 않으므로 픽셀 크기가 320일 때를 선택해야겠다.  

## 2026-11-08 rule for dropping training photos: not outdoor street photos (Track A, on top of drop_car_closeups)
- rule: 도시의 실외 길거리 사진이 아닌 것(실내, 셀카, 음식)은 제외한다.
- reason: 과제의 목표와 맞지 않는 사진이다. 상관없는 규칙을 배울 수 있기에 제거한다.
- how I will look: all training photos whose probability for their own city is below 0.3 in suspects_baseline_seed0.csv (from the run on every photo), for all five cities.

## 2026-11-09 b_mnv3_320_bal (Track B)
- changed: `--balance` (every city drawn equally often) on top of b_mnv3_320; everything else as in b_mnv3_320 (mobilenet_v3_large IMAGENET1K_V2 at 320, 4 epochs, all 44257 starter photos, learning rate 3e-4, batch size 64), on Colab, with `--keep`
- why: 부산의 사진이 도쿄 사진의 절반도 안 된다. 거의 모든 실험에서 하위권에 위치한 부산에 비해 도쿄는 거의 모든 실험에서 상위권에 위치했으므로 사진의 양이 학습의 질을 좌우하나 궁금해졌다. 
- validation: 0.5527 (before: b_mnv3_320 0.5494)
  - b_mnv3_320_bal: seoul 0.5741, busan 0.4986, tokyo 0.5609, osaka 0.5028, taipei 0.6273
  - b_mnv3_320:     seoul 0.6144, busan 0.4540, tokyo 0.6774, osaka 0.4008, taipei 0.6005
  - training time 2452.6 s (40.9 min), b_mnv3_320 2444.7 s (40.7 min); check_submission: format and limits: OK
- what it means: 전체 점수의 변화는 +0.33 정도로 이는 운의 크기와 비슷한 값이다. 따라서 효과가 좋았다고 보긴 어렵다. 다만 도시별로는 꽤 큰 변동이 일어났는데 같은 나라에 두 도시의 점수가 서로 반대로 움직여 전체 점수의 변동을 상쇄하고 있었다. 오사카는 10.2점이 상승하고 도쿄는 11.6점이 하락하고, 부산은 4.5점이 상승하고 서울 4점이 하락하는 식으로 말이다. 점수가 제일 높은 도시와 낮은 도시의 차이가 27.6점에서 12.8점으로 줄은 걸 보면 점수들이 이전보다 고르게 분포됐음을 확인할 수 있다. 나는 사진을 보여주는 빈도가 모델이 헷갈릴 때 어느 도시로 예측하는지에 영향을 미친다는 것이 도시 각각으로 증명됐다고 판단했다.

## 2026-11-09 drop_not_street (Track A)
- changed: on top of drop_car_closeups, 1672 more training photos dropped by the rule "도시의 실외 길거리 사진이 아닌 것(실내, 셀카, 음식)"; same starter recipe, seed 0, on Colab
  - sheets looked at: every selected photo whose probability for its own city was below 0.3 in suspects_baseline_seed0.csv (`scripts/draw_below.py --below 0.3`, 89 sheets: seoul 19, busan 12, tokyo 21, osaka 23, taipei 14)
  - dropped: seoul 359, busan 251, tokyo 446, osaka 323, taipei 293
  - final selection: 42411 photos (seoul 10914, busan 4789, tokyo 12894, osaka 6870, taipei 6944)
- why: 과제의 목표와 맞지 않는 사진이다. 상관없는 규칙을 배울 수 있기에 제거한다.
- validation: 0.4999 (before: drop_car_closeups 0.4983; baseline seed 0 0.4954, seed 1 0.4917)
  - drop_not_street:   seoul 0.5823, busan 0.4079, tokyo 0.6125, osaka 0.3529, taipei 0.5439
  - drop_car_closeups: seoul 0.5667, busan 0.3820, tokyo 0.6503, osaka 0.3670, taipei 0.5252
  - baseline seed 0:   seoul 0.5647, busan 0.3813, tokyo 0.6344, osaka 0.3398, taipei 0.5568
  - baseline seed 1:   seoul 0.5552, busan 0.3863, tokyo 0.6125, osaka 0.3811, taipei 0.5234
  - training time 2311.5 s (38.5 min)

## 2026-11-09 b_mnv3_320_bal_e8 (Track B)
- changed: `--epochs 8` instead of 4 on top of b_mnv3_320_bal; everything else as in b_mnv3_320_bal (mobilenet_v3_large IMAGENET1K_V2 at 320, `--balance`, all 44257 starter photos, learning rate 3e-4, batch size 64), on Colab, with `--keep`
- why: —balance로 도시별 점수를 고르게 만들었으니 이 상태에서 더 오래 학습해 같은 나라의 도시를 구별하는 능력을 향상해 전체 점수를 높이고 싶다. 마침 Track B는 학습량 제한이 없기도 하니 학습량을 2배 늘려보려고 한다.

## 2026-11-10 balanced (Track A)
- changed: on top of drop_not_street (same 42411 photos), `sample_weights` in recipe.py gives each photo 1 / the number of photos of its city, so every city is drawn equally often; nothing else changed; seed 0, on Colab
- why: Track B에서 도시 비율을 맞춰 같은 빈도로 사진을 보여줬을 때, 점수를 고르게 만드는 효과를 볼 수 있었다. 애매하면 사진이 많은 도시로 찍는 빈도가 줄어든 것이다. 따라서 해당 효과를 Track A에서도 적용해보려 한다.

## Next plan
Track B에선 사진을 직접 추가해볼 예정이다. 실내 사진은 제외하고 철저히 실외 사진으로 배경 중심에 사진을 선별해 넣으면 학습이 수월하지 않을까 생각한다. 물론 도시당 사진 몇십장만으로는 효과가 미미할 거라고 생각해 추가할 사진의 양도 늘리고, 도시일 확률 0.3 이하인 사진을 suspects 시트로 만들어 전부 검토한 다음, 도시를 특정하기 어려운 대상 중심의 음식 사진, 셀카 등을 스타터 사진에서 제외해볼 예정이다. 
