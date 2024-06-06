export interface Question {
    question_id: number;
    text: string;
    image?: string;
    position: number;
    answers: Answer[];
}

export interface Answer {
    answer_id: number;
    text: string;
    isCorrect: boolean;
}

export interface Quizz {
    id: number;
    question: Question;
    answers: Answer[];
}
