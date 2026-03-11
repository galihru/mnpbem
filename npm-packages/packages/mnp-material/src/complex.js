export function complex(re = 0, im = 0) {
  return { re: Number(re), im: Number(im) };
}

export function add(a, b) {
  return complex(a.re + b.re, a.im + b.im);
}

export function sub(a, b) {
  return complex(a.re - b.re, a.im - b.im);
}

export function mul(a, b) {
  return complex(a.re * b.re - a.im * b.im, a.re * b.im + a.im * b.re);
}

export function div(a, b) {
  const denom = b.re * b.re + b.im * b.im;
  if (denom === 0) {
    throw new Error("Division by zero complex number");
  }
  return complex((a.re * b.re + a.im * b.im) / denom, (a.im * b.re - a.re * b.im) / denom);
}

export function sqrtComplex(z) {
  const r = Math.hypot(z.re, z.im);
  const re = Math.sqrt((r + z.re) / 2);
  const imSign = z.im < 0 ? -1 : 1;
  const im = imSign * Math.sqrt(Math.max((r - z.re) / 2, 0));
  return complex(re, im);
}

export function fromReal(x) {
  return complex(x, 0);
}
