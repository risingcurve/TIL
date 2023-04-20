import React from "react";
import CharacterCount from "./CharacterCount";
import TextInput from "./TextInput";

const CharacterCounter = () => {
    return (
        <div>
            <TextInput />
            <CharacterCount />
        </div>
    );
};

export default CharacterCounter;