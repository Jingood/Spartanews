# SpartaNews

## 🖥️ 프로젝트 소개

#### SpartaNews : 다양한 언론들의 기사, 뉴스들을 볼 수 있는 사이트, 

#### 혹은 본인이 직접 기사, 뉴스들을 작성 할 수 있는 사이트

#### 🧭 목표 : DRF를 확실하게 사용해서 배포까지 가보자!!

#### 🕰️ 개발 기간
- 2024.05.03. ~ 2024.05.09.
  - 2024.05.03 : ERD 작성, API 구상하기, 개발일정 정하기, 업무분배
  - 2024.05.04 ~ 2024.05.06 : 휴식 or 시간날때 코딩
  - 2024.05.07 : API 개발 및 테스트, 일정조율
  - 2024.05.08 : 현황체크 및 테스트, 배포일정 정하기
  - 2024.05.09 : 테스트 후 배포 / 발표준비

### 💻 배포
- http://3.39.22.53/

#### 🤼멤버구성
- 박진수(팀장) : 뉴스 게시판
- 장민규      : 회원
- 김보인      : 찜하기
- 장석천      : 댓글, 좋아요

#### ⚙️ 개발 환경
- Python : Django, DRF
- DB : SQlite

#### 📌주요기능
- 회원
  - 회원가입
  - 로그인
  - 로그아웃
  - 프로필 조회
    - 작성한 게시물 조회
    - 작성한 댓글 조회
    - 찜한 게시물 조회
- 뉴스 게시판
  - 게시글 CRUD
- 댓글
  - 댓글 CRUD
  - 대댓글 CRUD
- 좋아요
  - 게시판/댓글 좋아요
- 찜
  - 게시글 찜하기

#### ERD
---
![스크린샷 2024-05-09 오후 8 19 07](https://github.com/Jingood/Spartanews/assets/60863619/4cb61378-fa12-4362-95e2-c01e4821dfd7)
---

#### API

##### Accounts

<img src=https://velog.velcdn.com/images/jingood/post/9df138ad-8216-4f11-9e42-348ef2e492d0/image.png>
<img src="https://velog.velcdn.com/images/jingood/post/b4e9652c-2156-41cc-99b2-d1006b5e22ff/image.png" width=300/>

##### News
<img src=https://velog.velcdn.com/images/jingood/post/180e9d83-e23a-44dc-b7d7-e3952b71246e/image.png>
<img src=https://velog.velcdn.com/images/jingood/post/59b4a599-d012-4a88-abf6-a6a3022abf24/image.png>

##### Comments
<img src=https://velog.velcdn.com/images/jingood/post/cea5891a-3f9c-4998-a2b4-4f2b4fee32a0/image.png>
<img src=https://velog.velcdn.com/images/jingood/post/c190de3e-0f98-4cbb-b939-58d99e468a57/image.png>

##### Likes
<img src=https://velog.velcdn.com/images/jingood/post/3d61a931-9bb8-4bdf-bc03-c8c5f1c1a5a6/image.png>

##### Jjim
<img src=https://velog.velcdn.com/images/jingood/post/290f01f9-e919-4374-929e-168582bbc186/image.png>
