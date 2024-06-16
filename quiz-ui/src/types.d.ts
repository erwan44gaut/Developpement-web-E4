export interface Question {
    id: number;
    title:string;
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

export interface Participation {
    answers: number[];
    playerName: string;
}

export interface Score {
    playerName: string;
    score: number;
}

export interface QuizInfo {
    scores: Score[];
    size: number;
}

export enum Grade {
    Excellent = 'Excellent',
    Good = 'Good',
    Average = 'Average',
    Poor = 'Poor'
}