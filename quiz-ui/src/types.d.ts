export interface Question {
    id: number;
    title: string;
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
