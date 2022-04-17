window.addEventListener("load", () => {
    const grid = new Isotope("section", {   //배치할 요소를 감싸고 있는 부모 요소명
        itemSelector: "article",   //배치할 요소명
        columnWidth: "article",    //넓이 값을 구할 요소명
        transitionDuration: "0.5s" //
    });

    // 클릭할 모든 버튼 요소를 변수에 저장
    const btns = document.querySelectorAll('main ul li');

    //버튼의 개수만큼 반복해서
    for (let el of btns) {
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
            for (let el of btns) {
                //각 버튼의 클래스명 "on"을 제거해 비활성화
                el.classList.remove('on')
            }
            //클릭한 대상만 선택해서 클래스명 on을 추가해 활성화
            e.currentTarget.classList.add('on')
        });
    }
});