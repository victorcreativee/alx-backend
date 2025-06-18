// 8-job.test.js
import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job.js';

describe('createPushNotificationsJobs', () => {
    const queue = kue.createQueue();

    before(() => {
        queue.testMode.enter();
    });

    afterEach(() => {
        queue.testMode.clear();
    });

    after(() => {
        queue.testMode.exit();
    });

    it('should throw an error if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs('not-an-array', queue)).to.throw('Jobs is not an array');
    });

    it('should create jobs in the queue', () => {
        const jobs = [
            {
                phoneNumber: '1234567890',
                message: 'test message 1'
            },
            {
                phoneNumber: '0987654321',
                message: 'test message 2'
            }
        ];

        createPushNotificationsJobs(jobs, queue);
        expect(queue.testMode.jobs.length).to.equal(2);
        expect(queue.testMode.jobs[0].data).to.deep.equal(jobs[0]);
        expect(queue.testMode.jobs[1].data).to.deep.equal(jobs[1]);
    });
});
