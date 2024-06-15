import axios from 'axios';
import { type Participation, type Question, type Score, type QuizInfo } from '../types.d';

// Fonction pour récupérer le nombre total de questions
export const getTotalNumberOfQuestions = async (): Promise<number> => {
	const response = await axios.get('http://127.0.0.1:5000/quiz-info');
	return response.data.size;
};

// Fonction pour récupérer quizz-info
export const getQuizInfo = async (): Promise<QuizInfo> => {
	const response = await axios.get('http://127.0.0.1:5000/quiz-info');
	return response.data;
};

// Fonction pour mettre à jour une question
export const updateQuestion = async (question: Question): Promise<void> => {
	try {
		const token = sessionStorage.getItem('authToken');
		if (!token) {
			throw new Error('No auth token found');
		}
		const response = await axios.put(
			`http://127.0.0.1:5000/questions/${question.id}`,
			question,
			{
				headers: {
					'Authorization': `Bearer ${token}`
				}
			}
		);
		return response.data;
	} catch (error) {
		console.error('Error updating question:', error);
		throw error;
	}
};

// Fonction pour suprimer une question
export const deleteQuestion = async (question: Question): Promise<void> => {
	try {
		const token = sessionStorage.getItem('authToken');
		if (!token) {
			throw new Error('No auth token found');
		}
		const response = await axios.delete(
			`http://127.0.0.1:5000/questions/${question.id}`,
			{
				headers: {
					'Authorization': `Bearer ${token}`
				}
			}
		);
		return response.data;
	} catch (error) {
		console.error('Error deleting question:', error);
		throw error;
	}
};

// Fonction pour créer une question
export const createQuestion = async (question: Question): Promise<void> => {
	try {
		const token = sessionStorage.getItem('authToken');
		if (!token) {
			throw new Error('No auth token found');
		}
		const response = await axios.post(
			'http://127.0.0.1:5000/questions',
			question,
			{
				headers: {
					'Authorization': `Bearer ${token}`
				}
			}
		);
		return response.data;
	} catch (error) {
		console.error('Error creating question:', error);
		throw error;
	}
};

// Fonction pour récupérer une question par position
export const getQuestionByPosition = async (position: number): Promise<Question> => {
	const response = await axios.get('http://127.0.0.1:5000/questions', {
		params: { position }
	});
	return response.data;
};

// Fonction pour enregistrer un score
export const saveScore = async (participation: Participation): Promise<number | null> => {
	try {
		const response = await axios.post('http://127.0.0.1:5000/participations', participation);
		return response.data.score;
	} catch (error) {
		console.error('Error saving score:', error);
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

// Fonction pour l'authentification
export const authenticate = async (password: string): Promise<string | null> => {
	try {
		const response = await axios.post('http://127.0.0.1:5000/login', { password });
		return response.data.token;
	} catch (error) {
		console.error('Error authentication:', error);
		throw error;
	}
};
