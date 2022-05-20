# Final PJT

<hr/>

[toc]

<hr/>

## 팀원
- 팀장 : 이동주
- 팀원 : 박세호

## 일정 
| 요일 | 예정                                          |          |      |
| ---- | --------------------------------------------- | -------- | ---- |
| 월   | BE 구현                                       | 완료유무 | 비고 |
|      | 모델 Article, Comment, User, Movie            | O        |      |
|      | 각 모델, serializer 구현                      | O        |      |
|      | view, serializer, model, url                  |          |      |
|      | admin 뷰 구현                                 |          |      |
| 화   | FE 구현 (Home, Profile, Article, Comment)     |          |      |
|      | router URl 설정                               |          |      |
|      | API 호출 경로 설정                            |          |      |
|      | Component, Views, Vuex 구현                   |          |      |
|      | i) 게시판(Articles) CRUD 구현                 |          |      |
|      | ii) 댓글 CRUD 구현                            |          |      |
|      |                                               |          |      |
| 수   | FE 구현 ( Movie)                              |          |      |
|      | Component, Views, Vuex 구현                   |          |      |
|      | i) 좋아요(Movie-user), 팔로우(User-User) 구현 |          |      |
|      | ii) 영화추천 알고리즘 구현(BE에 구현)         |          |      |
| 목 : | CSS 마무리(Bootstrap)                         |          |      |






## 데이터베이스 및 URL
### 데이터베이스

![](./README.assets/ERD.jpg)








### API_URL(BackEnd, Django)

|         | URL패턴                      | 역할                    |
| ------- | ---------------------------- | ----------------------- |
| User    | /login/                      | -                       |
|         | /logout/                     | -                       |
|         | /signup/                     | -                       |
|         | /profile/\<username>/        | user 정보 조회          |
| Article | /                            | 전체 article 조회(Home) |
|         | /articles/new/               | airtlcie 생성           |
|         | /aritlces/<article_pk>/      | article detail          |
|         | /articles/<article_pk>/edit/ | aritcle 수정            |
| Movie   | /movies/                     | 전체 영화 조회          |
|         | /movies/\<movie_pk>/         | movie detail            |
|         | /movies/recommendations/     | 영화 추천               |
| Raiting |                              |                         |
|         |                              |                         |
| error   | /404/                        | error 페이지 통합       |



### router_URL(FrontEnd, Vue)

|      |
| ---- |



## 구조 설계

###  App.vue
- header 에 navbar 로 각 router 생성(Home, Movie, Article, User) 
- 로그인 상태에 따라 navbar 구성이 변경

#### Home()
**초기화면**

- 웹페이지 소개
- router 이동
	- Movie 클릭시, 전체 영화조회
	- Article 클릭시, 게시글 조회
	- User 클릭시, profile, login, logout ( 로그인 상태에 따라)

#### Movie(url: "/")
- card component 로 나열(5\*10)
	- 영화 card 선택시, 해당 영화의 상세 정보 조회
	- user 가 login 시에 해당 영화의 평점 기입 가능.
- 상단에 추천 버튼
	- 클릭시, 알고리즘에 의해서 추천 영화 제시
		- 알고리즘은 API 또는 기존 데이터를 이용하여 설계

#### Article(url:)
- 전체 Article 조회
	- Bootstrap vue 를 활용하여 List group으로 구성
	- Article의 말머리, 제목, 작성자, 좋아요갯수 로 각 list item 구성
	- Article list item 클릭시, 해당 Article 상세 페이지로 이동
		- Article title, content, Comment 로 구성
- Article create 버튼
	- 클릭시 Article 작성 페이지(/articles/new/ )로 이동



**작업기록**

- 2022.05.20
	
	- 작업시작.
	
	1. README(작업 일정, DB설계, API_URL 설계, 구조 설계) 초안 작성
	1. BE에 필요한 Fixtures 생성(movies, genres)
	1. BE의 Movie, Raiting, Genre 등의 model 및 serializer 추가
	
	- 위 관련 views 작업 예정