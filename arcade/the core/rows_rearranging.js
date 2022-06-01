const matrix = [
  [2, 7, 1],
  [0, 2, 0],
  [1, 3, 1],
];

const matrix1 = [
  [2, 7, 1],
  [2, 8, 1],
  [3, 9, 1],
];

const matrix3 = [
  [6, 4],
  [2, 2],
  [4, 3],
];
const solution = (matrix) => {
  let possible = true;
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[i].length; j++) {
      if (i !== j) {
        possible =
          possible &&
          (matrix[i].every((element, index) => element > matrix[j][index]) ||
            matrix[i].every((element, index) => element < matrix[j][index]));
      }
    }
  }
  return possible;
};

console.log(solution(matrix3));
