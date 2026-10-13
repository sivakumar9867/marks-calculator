(() => {
  const form = document.getElementById('marks-form');
  if (!form) return;
  const fields = ['python', 'c', 'dsa'].map(id => document.getElementById(id));
  const totalNode = document.getElementById('live-total');
  const averageNode = document.getElementById('live-average');
  const meter = document.getElementById('live-meter-fill');
  const rows = [...document.querySelectorAll('.subject-row')];

  function update() {
    const values = fields.map(field => field.value.trim() === '' ? null : Number(field.value));
    values.forEach((value, index) => {
      const row = rows[index];
      const track = row.querySelector('.row-track span');
      const valid = value !== null && Number.isInteger(value) && value >= 0 && value <= 100;
      track.style.width = valid ? `${value}%` : '0%';
      track.style.background = valid && value < 35 ? 'var(--red)' : 'var(--acid)';
      row.classList.toggle('invalid-mark', value !== null && !valid);
    });
    const complete = values.every(value => value !== null && Number.isInteger(value) && value >= 0 && value <= 100);
    if (!complete) {
      totalNode.innerHTML = '— <small>/ 300</small>';
      averageNode.innerHTML = '—<small>%</small>';
      meter.style.width = '0%';
      return;
    }
    const total = values.reduce((sum, value) => sum + value, 0);
    const average = total / 3;
    totalNode.innerHTML = `${total} <small>/ 300</small>`;
    averageNode.innerHTML = `${average.toFixed(1)}<small>%</small>`;
    meter.style.width = `${average}%`;
  }

  fields.forEach(field => field.addEventListener('input', update));
  form.addEventListener('submit', event => {
    const name = document.getElementById('name');
    const firstInvalid = fields.find(field => field.value.trim() === '' || !Number.isInteger(Number(field.value)) || Number(field.value) < 0 || Number(field.value) > 100);
    if (!name.value.trim() || firstInvalid) {
      event.preventDefault();
      if (!name.value.trim()) name.focus();
      else firstInvalid.focus();
      if (firstInvalid) firstInvalid.setCustomValidity('Enter a whole number from 0 to 100.');
      form.reportValidity();
    }
  });
  fields.forEach(field => field.addEventListener('input', () => field.setCustomValidity('')));
  update();
})();
