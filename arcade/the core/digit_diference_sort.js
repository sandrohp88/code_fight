const a = [152, 23, 7, 887, 243];
const solution = (arr) => {
  let transformedArray = [];
  for (let i = 0; i < arr.length; i++) {
    // extract the digits
    const digits = arr[i]
      .toString()
      .split("")
      .map((digit) => +digit);
    //   find min and max digits
    const { max, min } = maxMin(digits);
    transformedArray.push({
      index: i,
      number: arr[i],
      max,
      min,
      diff: max - min,
    });
  }
  //   sort based on criteria
  transformedArray.sort((a, b) => {
    if (a.diff === b.diff) return b.index - a.index;
    return a.diff - b.diff;
  });
  transformedArray.map((element) => element.number);
};
const maxMin = (arr) => {
  let max = arr[0];
  let min = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (max < arr[i]) {
      max = arr[i];
    }
    if (min > arr[i]) {
      min = arr[i];
    }
  }
  return { max, min };
};
solution(a);
