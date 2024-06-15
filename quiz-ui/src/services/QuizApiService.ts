import axios from 'axios';
import { type Participation, type Question, type Score } from '../types.d';

// Fonction pour récupérer le nombre total de questions
export const getTotalNumberOfQuestions = async (): Promise<number> => {
	const response = await axios.get('http://127.0.0.1:5000/quiz-info');
	return response.data.size;
};

// Fonction pour récupérer une question par position
export const getQuestionByPosition = async (position: number): Promise<Question> => {
	const response = await axios.get('http://127.0.0.1:5000/questions', {
		params: { position }
	});
	return response.data;
};

// Fonction pour enregistrer un score
export const saveScore = async (participation: Participation): Promise<void> => {
	try {
		const response = await axios.post('http://127.0.0.1:5000/participations', participation);
		return response.data;
	} catch (error) {
		console.error('Error saving score:', error);
		throw error;
	}
};

//  Fonction pour récupérer le dernier score du joueur
export const getLastScorePlayer = async (playerName: string): Promise<number | null> => {
	try {
		const response = await axios.get('http://127.0.0.1:5000/quiz-info');
		const scores: Score[] = response.data.scores;

		const playerScore = scores.find(score => score.playerName === playerName);
		
		return playerScore ? playerScore.score : null;
	} catch (error) {
		console.error('Error fetching scores:', error);
		throw error;
	}
};

export const getAllScoresForPlayer = async (playerName: string): Promise<number[]> => {
	try {
		const response = await axios.get('http://127.0.0.1:5000/quiz-info');
		const scores: Score[] = response.data.scores;

		const playerScores = scores
			.filter(score => score.playerName === playerName)
			.map(score => score.score)
			.sort((a, b) => b - a); // Trier les scores en ordre décroissant
		
		return playerScores;
	} catch (error) {
		console.error('Error fetching scores:', error);
		throw error;
	}
};

export const getAllScores = async (): Promise<Score[]> => {
	try {
		const response = await axios.get('http://127.0.0.1:5000/quiz-info');
		const scores: Score[] = response.data.scores;
		
		return scores;
	} catch (error) {
		console.error('Error fetching scores:', error);
		throw error;
	}
};

export const getBestScoreForPlayer = async (playerName: string): Promise<number | null> => {
	try {
		const response = await axios.get('http://127.0.0.1:5000/quiz-info');
		const scores: Score[] = response.data.scores;

		const playerScores = scores
			.filter(score => score.playerName === playerName)
			.map(score => score.score);

		if (playerScores.length === 0) {
			return null;
		}

		const bestScore = Math.max(...playerScores);
		return bestScore;
	} catch (error) {
		console.error('Error fetching scores:', error);
		throw error;
	}
};

