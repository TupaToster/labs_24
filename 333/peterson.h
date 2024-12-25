struct peterson {
	int turn;
	int interested[2];
};

void peterson_init(struct peterson* p) {
	p->turn = 0;
	p->interested[0] = 0;
	p->interested[1] = 0;
}

void peterson_lock(struct peterson* p, int pnum) {
	p->interested[pnum] = 1;
	p->turn = pnum;
	while (p->turn == pnum && p->interested[1-pnum] != 0);
}

void peterson_unlock(struct peterson* p, int pnum) {
	p->interested[pnum] = 0;
}
