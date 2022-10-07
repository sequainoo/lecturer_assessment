// get hidden data / html elements 
function getHiddenBlobs() {
  const hidden = $('.hide');
  let i = 0;
  const hidden_array = [];
  while (i < hidden.length) {
    hidden_array.push($(hidden[i]));
    i++;
  }
  return hidden_array;
}
