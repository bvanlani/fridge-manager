const socket = io(`http://${window.location.host}`);

const cap = (s) => s.replace(/\b\w/g, (c) => c.toUpperCase());

// Handles "fresh apple", "fresh_apple", "Fresh-Apple", "freshapple", "apple fresh"
function parseLabel(raw) {
  const clean = String(raw).toLowerCase().replace(/[_\-]+/g, ' ').trim();
  const match = clean.match(/fresh|rotten/);
  const condition = match ? match[0] : null;
  const fruit = clean.replace(/fresh|rotten/, '').replace(/\s+/g, ' ').trim();
  return { condition, fruit: fruit || clean };
}

socket.on('classifications', (message) => {
  const entries = typeof message === 'string' ? JSON.parse(message) : message;
  if (!entries || entries.length === 0) return;

  const top = entries.reduce((a, b) => (b.confidence > a.confidence ? b : a));
  console.log('raw label:', top.content, 'confidence:', top.confidence);

  const { condition, fruit } = parseLabel(top.content);

  document.getElementById('fruit').textContent = cap(fruit);

  const cond = document.getElementById('condition');
  const base = 'rounded-full font-bold px-4 py-1 ';
  if (condition === 'fresh') {
    cond.textContent = 'Fresh';
    cond.className = base + 'bg-lime-100 text-lime-700';
  } else if (condition === 'rotten') {
    cond.textContent = 'Rotten';
    cond.className = base + 'bg-red-100 text-red-600';
  } else {
    cond.textContent = 'Unknown';
    cond.className = base + 'bg-slate-100 text-slate-600';
  }
});