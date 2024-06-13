export interface Question {
    id: number;
<<<<<<< HEAD
    title: string;
=======
    title:string;
>>>>>>> 514e048737177fac95cd616b9198dd8bf3037738
    text: string;
    image: string;
    position: number;
    possibleAnswers: Answer[];
}

export interface Answer {
    answer_id: number;
    text: string;
    isCorrect: boolean;
}
