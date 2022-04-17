// 전역변수(global variable) 초기화
const frame = 'section';
const box = "article";
const speed = "0.5s";
const activeClass = "on";
// 클릭할 모든 버튼 요소를 변수에 저장
const btn = document.querySelectorAll('main ul li');
let grid;   //플러그인의 정보값이 담길 변수를 이곳에 전역으로 설정

window.addEventListener("load", ()=>{
    //초기화함수 호출
    init();
    //클릭이벤트에 따른 필터처리
    filter(btn);
});

//초기화 함수 정의
function init(){
    //변수 grid에 담길 결과 값이 다른 함수인 filter에서도 활용되어야 하므로
    //전역변수 선언
    grid = new Isotope(frame, {   //배치할 요소를 감싸고 있는 부모 요소명
        itemSelector: box,   //배치할 요소명
        columnWidth: box,    //넓이 값을 구할 요소명
        transitionDuration: speed //
    });
}

function filter(arr) {
    //버튼의 개수만큼 반복해서
    for (let el of arr) {
        //각 버튼에 클릭 이벤트 연결
        el.addEventListener("click", e => {
            e.preventDefault();
            //a태그는 하이퍼링크 기능을 가지고 있는데, 회피함

            //변수 sort에 클릭한 대상의 자식인 a요소의 href 속성 값 지정
            const sort = e.currentTarget.querySelector("a").getAttribute("href");

            //grid에 저장된 결과값을 재정렬 기능 연결
            grid.arrange({
                //옵션값으로 sort 변수값 지정
                filter: sort
            });

            //다시 모든 버튼의 개수만큼 반복해서
            for (let el of arr) {
                //각 버튼의 클래스명 "on"을 제거해 비활성화
                el.classList.remove(activeClass)
            }
            //클릭한 대상만 선택해서 클래스명 on을 추가해 활성화
            e.currentTarget.classList.add(activeClass)
        });
    }
};
// Magnitic Popup 실행구문
$(document).ready(function () {

    $('.image-popup-vertical-fit').magnificPopup({
        type: 'image',
        closeOnContentClick: true,
        mainClass: 'mfp-img-mobile',
        image: {
            verticalFit: true
        }
    });

    //무한스크롤 적용

/*     //문서 객체 추가 함수
    let appendDocument = function () {
        for (let i = 0; i < 20; i++) {
            //문서 객체를 생성
            $('<h1>무한 스크롤</h1>').appendTo('body');
        }
    };
    //초기에 문서 객체를 추가
    // appendDocument()

    //이벤트를 연결
    $(window).scroll(function () {
        //변수 선언
        let scrollHeight = $(window).scrollTop() + $(window).height()
        let documentHeight = $(document).height()

        //검사
        if (scrollHeight == documentHeight) {
            appendDocument();
        }
    }); */

    let appendDocument = function() {
        for(let i = 0; i < 20; i++){
            $('<h1>무한 스크롤</h1>').appendTo('body')
        }
    }

    $(window).scroll(function() {
        console.log("스크롤의 위치 높이", $(window).scrollTop())
        console.log("윈도우 높이", $(window).height())
        console.log("html문서", $(document).height())
        let scrollHeight = $(window).scrollTop() + $(window).height()
        let documentHeight = $(document).height()

        if(scrollHeight==documentHeight) {
            appendDocument()
        }
    })
});