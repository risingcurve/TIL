import React from "react";
import { useRecoilState } from "recoil";
import { charCountState } from "./RecoilState";

const CharacterCount = () => {
    const count = useRecoilState(charCountState);
    return <div>Character Count : {count}</div>;
};

export default CharacterCount;