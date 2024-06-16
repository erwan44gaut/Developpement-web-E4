import axios from 'axios';
import { type Participation, type Question, type Score, type QuizInfo, Grade } from '../types.d';

// Fonction pour récupérer le nombre total de questions
export const getTotalNumberOfQuestions = async (): Promise<number> => {
	const quizInfo = await getQuizInfo();
	return quizInfo.size;
};

// Fonction pour récupérer le nombre total de questions
export const getTotalNumberOfScores = async (): Promise<number> => {
	const quizInfo = await getQuizInfo();
	return quizInfo.scores.length;
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

const calculateGrade = (percentage: number): Grade => {
	switch (true) {
	case percentage >= 90:
		return Grade.Excellent;
	case percentage >= 75:
		return Grade.Good;
	case percentage >= 50:
		return Grade.Average;
	default:
		return Grade.Poor;
	}
};

export const SaveScoreWithGrade = async (participation: Participation): Promise<{ score: number, grade: Grade } | null> => {
	try {
		const score = await saveScore(participation);
		const numberOfQuestions = await getTotalNumberOfQuestions();

		// Calculate the percentage score
		if (score != null){
			const percentage = (score / (numberOfQuestions * 10)) * 100; // Assuming each question is scored out of 10

			// Determine the grade based on the percentage score
			const grade = calculateGrade(percentage);

			return { score, grade };
		}
		return null;

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

// Fonction pour récupérer les counts corrects et incorrects pour une question donnée
export const getCorrectIncorrectCountsForQuestion = async (questionId: number): Promise<{ is_correct: number, is_not_correct: number }> => {
	const response = await axios.get(`http://127.0.0.1:5000/participation-answers/${questionId}`);
	return response.data;
};

// Fonction pour récupérer les counts corrects et incorrects pour chaque question
export const getCorrectIncorrectCounts = async (): Promise<{ questionId: number, is_correct: number, is_not_correct: number }[]> => {
	const totalQuestions = await getTotalNumberOfQuestions();
	const counts: { questionId: number, is_correct: number, is_not_correct: number }[] = [];

	for (let position = 1; position <= totalQuestions; position++) {
		const question = await getQuestionByPosition(position);
		const correctIncorrectCounts = await getCorrectIncorrectCountsForQuestion(question.id);
		counts.push({
			questionId: question.id,
			is_correct: correctIncorrectCounts.is_correct,
			is_not_correct: correctIncorrectCounts.is_not_correct
		});
	}
	return counts;
};


