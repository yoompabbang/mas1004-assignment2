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
