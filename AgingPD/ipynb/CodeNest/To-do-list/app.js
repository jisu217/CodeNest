const addButton = document.querySelector('#add-button');

addButton.addEventListener('click', () => {
  const input = document.querySelector('#input'); // 사용자 입력 불러오기
  const text = input.value.trim(); // trim() 문자열 양 끝 공백 제거

  if (text !== '') {
    addToList(text);
    input.value = ''; // 사용자의 입력칸 빈칸으로 리셋
    input.focus(); // 입력창에 포커스 부여
  }

  function addToList(text) {
  const list = document.querySelector('#list');

  const newListItem = document.createElement('li'); // 새로운 li 요소를 만듬
  newListItem.classList.add('list-item'); // list-item 클래스를 더해줌

  newListItem.innerHTML = text; //사용자 입력 문자를 li사이에 넣음

  list.appendChild(newListItem); // 리스트에 새로 만든 li를 추가
}

});