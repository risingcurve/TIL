import { Component } from "react";

class Counter extends Component {
    state = {
        number: 0,
        fixedNumber: 0
    }



    // constructor(props) {
    //     super(props)
    //     // state의 초기값 설정
    //     this.state = {
    //         number: 0,
    //         fixedNumber: 0
    //     }
    // }

    render() {
        const { number, fixedNumber } = this.state; // state를 조회할 때는 this.state로 조회합니다.
        return (
            <div>
                <h1>{number}</h1>
                <h2>바뀌지 않는 값: {fixedNumber}</h2>
                <button
                    // onClick을 통해 버튼이 클릭되었을 때 호출할 함수를 지정
                    onClick={() => {
                        // this.setState를 사용하여 state에 새로운 값을 넣을 수 있습니다.
                        // this.setState({ number: number + 1 })
                        // this.setState({ number: this.state.number + 1 })
                        this.setState(PrevStete => {
                            return {
                                number: PrevStete.number + 1
                            }
                        })
                        // 위 코드와 아래 코드는 완전히 똑같은 기능을 합니다.
                        // 아래 코드는 함수에서 바로 객체를 반환한다는 의미입니다.
                        this.setState(PrevStete => {
                            return {
                                number: PrevStete.number + 1
                            }
                        })
                    }}
                >
                    +2
                </button>
                <button
                    // onClick을 통해 버튼이 클릭되었을 때 호출할 함수를 지정
                    onClick={() => {
                        this.setState(
                            {
                                number: number + 1
                            },
                            () => {
                                console.log('방금 setState가 호출되었습니다.')
                                console.log(this.state)
                            }
                        )
                    }}
                >
                    +1
                </button>
            </div>
        )
    }
}

export default Counter