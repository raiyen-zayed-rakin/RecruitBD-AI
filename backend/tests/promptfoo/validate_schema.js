export default (output, context) => {
  try {
    const parsed = JSON.parse(output);
    const expectedKeys = ['name', 'email', 'phone', 'location', 'summary', 'skills', 'experience', 'education', 'languages', 'certifications', 'references'];
    const hasKeys = expectedKeys.every(k => k in parsed);
    const isArray = Array.isArray(parsed.skills) && Array.isArray(parsed.experience) && Array.isArray(parsed.education);
    return hasKeys && isArray;
  } catch (e) {
    console.error(e);
    return false;
  }
};
