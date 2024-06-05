export interface Question {
    id: number;
    label: string;
    type: number;
}

export interface Answer {
    id: number;
    label: string;
    value: number;
}

export interface Quizz {
    id: number;
    question: Question;
    answers: Answer[];
}
