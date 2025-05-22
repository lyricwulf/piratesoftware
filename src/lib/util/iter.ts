export function iter<T>(value: T | T[] | null | undefined | false): T[] {
  if (!value) return [];
  if (Array.isArray(value)) return value;
  return [value];
}
