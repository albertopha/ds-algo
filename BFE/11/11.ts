type Func = (arg: any) => any

function pipe(funcs: Array<Func>): Func {
	return (arg) => funcs.reduce((acc, func) => func(acc), arg);
}

