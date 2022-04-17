//마우스 포인트 올리면 동영상 재생하기
/* 이벤트가 발생한 현재 요소 지정
https://www.w3schools.com/tags/av_met_play.asp
Play(), pause() : video/audio 요소에 적용 가능
e.currentTarget.querySelector("").play() */

const items = document.querySelectorAll('article')

for (let vi of items) {
    //마우스가 호버되었을때, 재생하도록 함
    vi.addEventListener('mouseenter', e => {
        e.currentTarget.querySelector('video').play()
    })
    //마우스가 떠났을 때, 재생정지
    vi.addEventListener("mouseleave", e=>{
        e.currentTarget.querySelector('video').pause()
    })
}