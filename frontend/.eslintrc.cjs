/* eslint-env node */
require('@rushstack/eslint-patch/modern-module-resolution');

module.exports = {
	root: true,
	'extends': [
		'plugin:vue/vue3-essential',
		'eslint:recommended',
		'@vue/eslint-config-typescript'
	],
	parserOptions: {
		ecmaVersion: 'latest'
	},
	rules: {
		// Règles de formatage
		'indent': ['error', 'tab'], // Indentation avec tab
		'semi': ['error', 'always'], // Toujours mettre un point-virgule à la fin des instructions
		'quotes': ['error', 'single'], // Utiliser des guillemets simples pour les chaînes de caractères
		'comma-spacing': ['error', { 'before': false, 'after': true }], // Espacement après la virgule, pas avant
		'object-curly-spacing': ['error', 'always'], // Espacement à l'intérieur des accolades des objets
		'array-bracket-spacing': ['error', 'never'], // Espacement à l'intérieur des crochets des tableaux
		'keyword-spacing': ['error', { 'before': true, 'after': true }], // Espacement autour des mots-clés
		'space-infix-ops': 'error', // Espacement autour des opérateurs
		'no-multi-spaces': 'error', // Pas de multiples espaces consécutifs

		// Règles de bonnes pratiques
		'no-console': 'warn', // Interdire l'utilisation de console.log() et autres dans le code de production
		'prefer-const': 'error', // Utiliser const lorsque la variable ne sera pas réassignée
		'prefer-template': 'error', // Utiliser les templates strings (`${variable}`)
		'no-useless-concat': 'error', // Éviter les concaténations inutiles de chaînes de caractères

		// Règles spécifiques à Vue.js
		'vue/no-unused-components': 'warn', // Avertissement pour les composants Vue non utilisés
	}
};
