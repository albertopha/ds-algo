/**
 * @param {string[]} paths
 * @return {string[][]}
 */
var findDuplicate = function(paths) {
    if (!paths || !paths.length) return [];
    const pathsContentMap = paths.reduce((map, path) => extractPath(path, map), {});
    return Object.values(pathsContentMap).filter((value) => value.length > 1);
};

function extractPath(path, map) {
    if (typeof path !== 'string' || path.length === 0) return [null, null];
    const splitted = path.split(' ');
    const rootPath = splitted[0];
    return splitted.slice(1).reduce((m, file) => {
        const [fileName, content] = extractFile(file);
        if (!m[content]) m[content] = [];
        m[content].push(`${rootPath}/${fileName}`);
        return map;
    }, map);
};

function extractFile(file) {
    const start = file.indexOf('(');
    const end = file.indexOf(')');
    const content = file.substring(start, end+1);
    const fileName = file.substring(0, start);
    return [fileName, content];
};
