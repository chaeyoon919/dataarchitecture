# dataarchitecture
- [Project summary](#da-design-server)
  - [Purpose](#purpose)
  - [Requirements](#requirements)
  - [How to install](#how-to-install)
- [How to use](#how-to-use)
- [Version History](#version-history)
- [Contacts](#contacts)
- [License](#license)

---

### Project summary

본 연구는 월간 거래 분석으로 제공되는 1) 월별 거래 분석 2) 지출 성향 분석 3) 월별 잉여 자금 산출 4) 다음 달 지출 예측 금액 제시 5) 목표 자금을 위한 방향성 제시 등과 같은 기능으로 '개인 맞춤 금융 포트폴리오 제시' 서비스를 제공한다. 이 서비스는 개인의 지출 계획은 물론 자금 관리까지 아우르는 장기적인 리포트를 제공함으로써 사용자들의 건강한 소비 습관을 심어주고 이는 건강한 경제 사회를 지속시킬 것이다.

#### Purpose

#### Requirements
* python >= 3.6.9

#### How to install
* Clone & Install

```sh
git clone https://github.com/

pip3 install -r requirements.txt
```

```

---

### How to use
{사전 지식 : 서비스 구동 방식}

본 서비스는 개인 맞춤 서비스이기 때문에 로그인 설정이 필요하다.
로그인 설정 후 개인 sms 카드 내역과 통장 내 입출금 목록을 연동하여 수입, 지출 데이터를 수집한다.

수집된 데이터는 전체, 식음료, 생활용품, 의류 등 카테고리 별로 분석되어 한 달동안의 지출 내역 및 패턴을 차트로 명확하게 분석한다. 또한 지출 패턴 분석을 통한 머신러닝 모델을 이용하여 다음 달의 지출 금액을 예측하여 제시한다. 

또한 자산 관리 영역을 다루기 위해 개인이 목표로 하는 자산 금액을 설정하고 투자 성향을 선택한다.
본인의 투자 성향과 지출 패턴을 바탕으로 잉여 자금이 발생하였을 시, 개인의 자산 목표에 다가갈 수 있는 투자 방안을 제시한다.
---

### Version History

* v.0.0.0 : 개발중

---

### Contacts


---

### License

Apache-2.0
